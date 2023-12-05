import SearchBar from "./SearchBar";
import RecipeList from "./RecipeList";
import { useEffect, useState } from "react";
import axios from "axios";

/**
 * 레시피 검색 페이지
 * @returns
 */
const RecipeSearcher = () => {
  const [recipes, setRecipes] = useState([]);

  useEffect(() => {
    const dataUrl = `${process.env.REACT_APP_SERVER}/api/recipe/`;
    axios
      ?.get(dataUrl, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        setRecipes(res.data);
      });
  }, []);

  return (
    <>
      <div className="flex flex-row">
        <SearchBar setRecipes={setRecipes}></SearchBar>
        <RecipeList recipes={recipes}></RecipeList>
      </div>
    </>
  );
};

export default RecipeSearcher;
