import { Stack, Pagination } from "@mui/material";
import { useState, useEffect } from "react";
import RecipePreview from "./RecipePreview";

const RecipeList = ({ recipes }) => {
  const [page, setPage] = useState(1);

  return (
    <>
      <div className="w-screen h-screen mx-auto pt-[100px] px-[32px] flex flex-row flex-wrap bg-backgroundGray overflow-y-scroll">
        {recipes.map((recipe) => (
          <RecipePreview key={recipe.recipe_id} recipe={recipe}></RecipePreview>
        ))}
      </div>
    </>
  );
};

export default RecipeList;
