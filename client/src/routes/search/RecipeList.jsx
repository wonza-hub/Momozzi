import RecipePreview from "./RecipePreview";

/**
 * 레시피 목록 컴포넌트
 * @param {object[]}
 * @returns
 */
const RecipeList = ({ recipes, isReadingRecipes }) => {
  return (
    <>
      {isReadingRecipes ? null : (
        <div className="w-screen h-screen pt-[100px] flex flex-row flex-wrap bg-backgroundGray/20 overflow-y-scroll">
          {recipes.map((recipe) => (
            <RecipePreview
              key={recipe.recipe_id}
              recipe={recipe}
            ></RecipePreview>
          ))}
        </div>
      )}
    </>
  );
};

export default RecipeList;
