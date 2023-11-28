// 테스트용 이미지
import bg from "../../img/fridge_bg.png";

const RecipePreview = ({ recipe }) => {
  const recipeThumbnail = recipe.thumbnail_url;
  const recipeDescription = recipe.description;
  const cuisineName = recipe.cuisine_name;

  return (
    <>
      <div className="w-[372px] h-[412px] pt-2 px-8 bg-white">
        <div className="thumbnail h-[328px] rounded-2xl overflow-hidden shadow-[rgba(13,_38,_76,_0.19)_0px_9px_20px]">
          <img
            className="w-full max-w-full h-full object-cover brightness-95"
            src={bg}
            alt={"recipeThumbnail"}
          />
        </div>
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
