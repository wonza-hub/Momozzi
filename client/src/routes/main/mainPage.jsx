import { useEffect, useState } from "react";
import axios from "axios";
import RecipePreview from "../search/RecipePreview";

const MainPage = () => {
  const [mostReviewedRecipes, setMostReviewedRecipes] = useState([]);
  const [mostFastRecipes, setMostFastRecipesURL] = useState([]);

  useEffect(() => {
    // GET: 리뷰 많은 레시피
    let mostReviewedRecipeURL = `${process.env.REACT_APP_SERVER}/api/recipe/top/`;
    axios?.get(mostReviewedRecipeURL)?.then((res) => {
      setMostReviewedRecipes(res.data);
    });
    // GET: 조리시간 빠른 레시피
    let mostFastRecipesURL = `${process.env.REACT_APP_SERVER}/api/recipe/fast/`;
    axios?.get(mostFastRecipesURL)?.then((res) => {
      setMostFastRecipesURL(res.data);
    });
  }, []);

  useEffect(() => {}, []);

  return (
    <>
      <div className="flex flex-col overflow-x-hidden overflow-y-auto">
        <div className="w-screen h-screen bg-[url('./img/main.png')] bg-repeat-x"></div>
        <div className="w-screen min-h-full h-[1000px] bg-[#FAF1E4]">
          <div className="m-auto w-[1500px] h-4/5 translate-y-20">
            <div className="w-full h-[430px]">
              <header className="text-2xl font-bold text-black">
                Top Review
              </header>
              <div className="flex flex-row">
                {mostReviewedRecipes.map((recipe) => (
                  <RecipePreview recipe={recipe}></RecipePreview>
                ))}
              </div>
            </div>
            <div className="w-full h-[430px] mt-2">
              <header className="text-2xl font-bold text-black">
                Fast Recipe
              </header>
              <div className="flex flex-row">
                {mostFastRecipes.map((recipe) => (
                  <RecipePreview recipe={recipe}></RecipePreview>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default MainPage;
