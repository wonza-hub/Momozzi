import SearchBar from "./SearchBar";
import RecipeList from "./RecipeList";
import { useEffect, useState } from "react";
import axios from "axios";
import { useQuery, useMutation } from "@tanstack/react-query";

/**
 * 레시피 검색 페이지
 * @returns
 */
const RecipeSearcher = () => {
  const {
    status,
    data: recipes,
    error,
    isLoading,
    isError,
  } = useQuery({
    queryKey: ["recipe-posts"],
    queryFn: async () => {
      const recipePostsURL = `${process.env.REACT_APP_SERVER}/api/recipe/`;
      return await axios.get(recipePostsURL).then((res) => res.data);
    },
  });

  return (
    <>
      <div className="flex flex-row">
        {/* <SearchBar setRecipes={setRecipes}></SearchBar> */}
        <RecipeList recipes={recipes} isLoading={isLoading}></RecipeList>
      </div>
    </>
  );
};

export default RecipeSearcher;
