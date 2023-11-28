import { Stack, Pagination } from "@mui/material";
import { useState, useEffect } from "react";
import RecipePreview from "./RecipePreview";

const RecipeList = ({ recipes }) => {
  const [page, setPage] = useState(1);

  return (
    <>
      <div className="w-screen mx-auto pt-[124px] px-[32px] h-screen bg-primary overflow-y-scroll">
        {recipes.map((recipe) => (
          <RecipePreview recipe={recipe}></RecipePreview>
        ))}
      </div>
    </>
  );
};

export default RecipeList;
