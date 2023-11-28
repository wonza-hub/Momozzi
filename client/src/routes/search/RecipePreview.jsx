// 테스트용 이미지
import bg from "../../img/fridge_bg.png";
import { Link } from "react-router-dom";

const RecipePreview = ({ recipe }) => {
  const recipeThumbnail = recipe.thumbnail_url;
  const recipeDescription = recipe.description;
  const cuisineName = recipe.cuisine_name;

  return (
    <>
      <div className="w-[296px] h-[416px] px-4 pt-4">
        <Link
          to={`../recipe/${recipe.recipe_id}`}
          state={{
            recipe,
          }}
        >
          <div className="thumbnail h-[328px] rounded-2xl overflow-hidden shadow-[rgba(13,_38,_76,_0.19)_0px_9px_20px]">
            <img
              className="w-full max-w-full h-full object-cover brightness-95"
              src={bg}
              alt={"recipeThumbnail"}
            />
          </div>
        </Link>
        <div className="pt-4 pl-2">
          <div className="description text-xl text-black">
            {recipeDescription}
          </div>
          <div className="cuisineName text-l text-black">{cuisineName}</div>
        </div>
      </div>
    </>
  );
};

export default RecipePreview;
