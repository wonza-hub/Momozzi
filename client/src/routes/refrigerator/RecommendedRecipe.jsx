import { Link } from "react-router-dom";

/**
 * 추천된 단일 레시피 컴포넌트
 * @param {ingredient}
 * @returns
 */
const RecommendedRecipe = ({ recipe }) => {
  return (
    <Link to={`../../recipe/${recipe.recipe_id}`}>
      <div
        className="text-lg w-full h-12 my-4 p-2 flex flex-row justify-between text-[#111111] text-left whitespace-nowrap hover:font-semibold duration-100"
        key={recipe.recipe_name}
      >
        <span className="w-48 text-primary truncate">{recipe.description}</span>
        <span className="w-26 text-primary truncate">
          {recipe.cuisine_name}
        </span>
      </div>
    </Link>
  );
};

export default RecommendedRecipe;
