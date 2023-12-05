import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import CircularProgress from "@mui/material/CircularProgress";

/**
 * 재료 등록 컴포넌트
 * @returns
 */
const IngredientRegistration = () => {
  const { fridgeId } = useParams();
  const [newIngredient, setNewIngredient] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const ingredientInputRef = useRef(null);

  const handleIngredientInputChange = () => {
    setNewIngredient(ingredientInputRef.current.value);
  };

  const addIngredient = (event) => {
    event.preventDefault();
    setIsLoading(true);

    if (!newIngredient) {
      return;
    }

    let requestBody = {
      refrigerator_id: fridgeId,
      ingredient_name: newIngredient,
    };
    // 미완성
    // POST: 냉장고 내 재료 추가
    const ingredientPostURL = `${process.env.REACT_APP_SERVER}/api/refrigerator_stores_ingredient`;
    axios
      ?.post(ingredientPostURL, requestBody)
      ?.then((res) => {
        if (res.status === 200) {
        }
      })
      ?.catch(() => console.log("post fail"));
  };

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
          <input
            onChange={handleIngredientInputChange}
            value={newIngredient}
            className="w-44 h-12 mr-6 px-4 py-2 bg-[#efefef]/80 rounded-xl border-2 border-primary outline-2 outline-primary text-lg text-black/90 hover:bg-[#efefef] focus:bg-[#efefef] duration-200"
            type="text"
            placeholder="재료 추가"
            ref={ingredientInputRef}
          />
        )}
        <button
          className="w-32 h-12 px-4 my-auto bg-primary/90 text-xl text-white rounded-xl hover:bg-primary duration-300"
          type={isLoading ? "button" : "submit"}
        >
          Add
        </button>
      </form>
    </>
  );
};

export default IngredientRegistration;
