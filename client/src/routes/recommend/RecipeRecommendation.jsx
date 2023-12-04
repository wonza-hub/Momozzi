import { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import RecipeList from "../search/RecipeList";
import axios from "axios";

const RecipeRecommendation = () => {
  const location = useLocation();
  const foodFilter = location.state && location.state.foodFilter;
  const { method, category } = foodFilter || {};

  const [recommendedRecipes, setRecommendedRecipes] = useState([]);

  useEffect(() => {
    if (method || category) {
      // 냉장고 내 재료로 만들 수 있는 레시피 불러오기
      const recommendUrl = `${process.env.REACT_APP_SERVER}/api/recipe/`;
      axios?.get(recommendUrl)?.then((res) => {
        setRecommendedRecipes(res.data);
      });
    }
  });

  return (
    <>
      <div className="flex flex-row">
        <RecipeList recommendedRecipes={recommendedRecipes}></RecipeList>
      </div>
    </>
  );
};

export default RecipeRecommendation;
