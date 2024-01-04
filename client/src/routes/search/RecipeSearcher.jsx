import SearchBar from "./SearchBar";
import RecipeList from "./RecipeList";
import { useEffect, useState } from "react";
import axios from "axios";
import { useQuery } from "@tanstack/react-query";

/**
 * 레시피 검색 페이지
 * @returns
 */
const RecipeSearcher = () => {
  const { data: recipes, isLoading: isReadingRecipes } = useGetRecipes();

  return (
    <>
      <div className="flex flex-row">
        {/* <SearchBar setRecipes={setRecipes}></SearchBar> */}
        <RecipeList
          recipes={recipes}
          isReadingRecipes={isReadingRecipes}
        ></RecipeList>
      </div>
    </>
  );
};

// REST: 레시피 목록 조회
const useGetRecipes = () => {
  return useQuery({
    queryKey: ["recipes"],
    queryFn: async () => {
      const recipePostsURL = `${process.env.REACT_APP_SERVER}/api/recipe/`;
      return await axios.get(recipePostsURL).then((res) => res.data);
    },
  });
};

export default RecipeSearcher;
