import { useState, useEffect, useRef } from "react";
import { redirect, useParams } from "react-router-dom";
import axios from "axios";
import CircularProgress from "@mui/material/CircularProgress";
import DropDown from "../../components/DropDown";

/**
 * 재료 등록 컴포넌트
 * @returns
 */
const IngredientRegistration = () => {
  const { fridgeId } = useParams();
  const [newIngredient, setNewIngredient] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [validIngredients, setValidIngredients] = useState([]);

  const addIngredient = (event) => {
    event.preventDefault();
    setIsLoading(true);

    if (!newIngredient) {
      return;
    }

    let requestBody = {
      refrigerator: fridgeId,
      ingredient_name: newIngredient,
    };
    console.log(requestBody);
    // POST: 냉장고 내 재료 추가
    const ingredientPostURL = `${process.env.REACT_APP_SERVER}/api/refrigerator_stores_ingredient/`;
    axios?.post(ingredientPostURL, requestBody)?.then((res) => {
      if (res.status === 200) {
        redirect(`/refrigerator/${fridgeId}`);
        window.location.reload();
      }
    });
  };

  useEffect(() => {
    // GET: 저장 가능 재료 목록 불러오기
    const validIngredientsURL = `${process.env.REACT_APP_SERVER}/api/ingredient/`;
    axios?.get(validIngredientsURL)?.then((res) => {
      if (res.status === 200) {
        const ingredientNames = res.data.map((item) => item.ingredient_name);
        setValidIngredients(ingredientNames);
      }
    });
  }, []);

  return (
    <>
      <form
        className="flex flex-row justify-end mt-6 mb-2"
        onSubmit={addIngredient}
      >
        {isLoading ? (
          <div className="w-44 h-12 pt-1 flex justify-center">
            <CircularProgress color="success" className="text-xl" />
          </div>
        ) : (
          <div className="my-auto">
            <DropDown
              menuItems={validIngredients}
              setArg={setNewIngredient}
            ></DropDown>
          </div>
        )}
        <button
          className="w-32 h-12 ml-4 my-auto mt-3 px-4 bg-primary/90 text-xl text-white rounded-xl hover:bg-primary duration-300"
          type={isLoading ? "button" : "submit"}
        >
          Add
        </button>
      </form>
    </>
  );
};

export default IngredientRegistration;
