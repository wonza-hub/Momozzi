import Inventory from "./Inventory";
import IngredientRegistration from "./IngredientRegistration";
import RecommendFilter from "./RecommendFilter";
import RecommendBtn from "./RecommendBtn";
import RecommendedRecipes from "./RecommendedRecipes";
import { useState, useEffect } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

/**
 * 냉장고 페이지
 * @returns
 */
const Refrigerator = () => {
  const { fridgeId } = useParams();
  const [storedIngredients, setStoredIngredients] = useState([]);
  const [recommendedRecipes, setRecommendedRecipes] = useState([]);
  const [method, setMethod] = useState("");
  const [category, setCategory] = useState("");

  useEffect(() => {
    // GET: 냉장고 내 재료 불러오기
    let openFridgeUrl = `${process.env.REACT_APP_SERVER}/api/refrigerator_stores_ingredient/?refrigerator=${fridgeId}`;
    axios?.get(openFridgeUrl)?.then((res) => {
      setStoredIngredients(res.data);
    });
  }, [fridgeId]);

  const onRecommendClick = () => {
    let body = {
      method,
      category,
      storedIngredients,
    };
    // 미완성
    // GET: 추천 레시피 불러오기
    const recommendURL = `${process.env.REACT_APP_SERVER}/api/`;
    axios
      ?.post(recommendURL, body, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        if (res.status === 200) {
          setRecommendedRecipes(res.data);
        }
      })
      ?.catch((e) => {});
  };

  return (
    <>
      <div className="absolute left-2/4 bg-[url('./img/fridge_bg.png')] w-2/4 h-screen"></div>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute bg-white/80 top-[450px] left-1/3 min-h-[560px] -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <Inventory storedIngredients={storedIngredients}></Inventory>
          <IngredientRegistration
            setStoredIngredients={setStoredIngredients}
          ></IngredientRegistration>
          <div className="flex flex-row justify-evenly">
            <RecommendFilter
              setRecommendedRecipes={setRecommendedRecipes}
              setMethod={setMethod}
              setCategory={setCategory}
            ></RecommendFilter>
            <RecommendBtn
              method={method}
              category={category}
              setRecommendedRecipes={setRecommendedRecipes}
              onRecommendClick={onRecommendClick}
            ></RecommendBtn>
          </div>
        </div>
        {recommendedRecipes ? (
          <RecommendedRecipes
            recommendedRecipes={recommendedRecipes}
          ></RecommendedRecipes>
        ) : null}
      </div>
    </>
  );
};

export default Refrigerator;
