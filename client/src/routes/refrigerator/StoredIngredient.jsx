/**
 * 냉장고 내 저장된 단일 재료 컴포넌트
 * @param {ingredient}
 * @returns
 */
const StoredIngredient = ({ ingredient }) => {
  return (
    <div className="text-lg my-2 px-14 flex flex-row text-[#111111]">
      <div className="w-52">
        <span className="ingredientType">{ingredient.type}</span>
      </div>
      <div className="w-48">
        <span className="ingredientName text-left">
          {ingredient.ingredient_name}
        </span>
      </div>
      <div className="w-24 pl-6">
        <span className="ingredientName">{ingredient.calories}</span>
      </div>
    </div>
  );
};

export default StoredIngredient;
