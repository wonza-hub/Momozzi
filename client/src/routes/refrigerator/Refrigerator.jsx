import Inventory from "./Inventory";
import IngredientRegistration from "./IngredientRegistration";
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

  useEffect(() => {
    // GET: 냉장고 내 재료 불러오기
    let openFridgeUrl = `${process.env.REACT_APP_SERVER}/api/refrigerator_stores_ingredient/?refrigerator=${fridgeId}`;
    axios?.get(openFridgeUrl)?.then((res) => {
      setStoredIngredients(res.data);
    });
  }, [fridgeId]);

  const onRecommendClick = () => {
    // GET: 추천 레시피 불러오기
    const recommendURL = `${process.env.REACT_APP_SERVER}/api/refrigerator/recommend/?refrigerator=${fridgeId}`;
    axios?.get(recommendURL)?.then((res) => {
      setRecommendedRecipes(res.data);
    });
  };

  return (
    <>
      <div className="absolute left-2/4 bg-[url('./img/fridge_bg.png')] w-2/4 h-screen"></div>
      <div className="relative min-w-screen min-h-screen bg-[#DBDBDB]/20">
        {/* box shadows - next.js */}
        <div className="absolute bg-white/80 top-[450px] left-1/3 min-h-[580px] -translate-x-2/4 -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
          <Inventory storedIngredients={storedIngredients}></Inventory>
          <IngredientRegistration
            setStoredIngredients={setStoredIngredients}
          ></IngredientRegistration>
          <RecommendBtn
            setRecommendedRecipes={setRecommendedRecipes}
            onRecommendClick={onRecommendClick}
          ></RecommendBtn>
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
