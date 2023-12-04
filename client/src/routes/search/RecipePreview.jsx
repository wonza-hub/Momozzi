// 테스트용 이미지
import bg from "../../img/fridge_bg.png";
import { Link } from "react-router-dom";

const RecipePreview = ({ recipe }) => {
  const recipeId = recipe.recipe_id;
  // 레시피 id에 따른 썸네일 처리 필요
  const recipeThumbnail = recipe.thumbnail_url;
  const recipeDescription = recipe.description;
  const cuisineName = recipe.cuisine_name;

  return (
    <>
      <div className="w-[296px] h-[416px] px-4 pt-4">
        <Link to={`../recipe/${recipeId}`}>
          <div className="thumbnail h-[328px] rounded-2xl overflow-hidden shadow-[rgba(13,_38,_76,_0.19)_0px_9px_20px] hover:-translate-y-1 duration-200 ease-in-out">
            <img
              className="w-full max-w-full h-full object-cover contrast-120 brightness-95"
              src={`../../img/recipe/{recipe_id}.png`}
              alt={"recipeThumbnail"}
            />
          </div>
        </Link>
        <div className="pt-4 pl-2">
          <div className="description text-xl text-black whitespace-nowrap overflow-hidden text-ellipsis">
            {recipeDescription}
          </div>
          <div className="cuisineName text-l text-black">{cuisineName}</div>
        </div>
      </div>
    </>
  );
};

export default RecipePreview;
