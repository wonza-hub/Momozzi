/**
 * 레시피 재료 목록 컴포넌트
 * @param {ingredients}
 * @returns
 */
const Ingredients = ({ ingredients }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-sm">
        Ingredients
      </header>
      <div className="ingredients mb-8 font-semibold text-xl text-white flex flex-row flex-wrap">
        {ingredients.map((ingredient) => (
          <div
            className="h-11 mr-3 mb-2 px-4 leading-10 bg-secondary text-center rounded-2xl"
            key={ingredient.id}
          >
            {ingredient.ingredient_name}
          </div>
        ))}
      </div>
    </>
  );
};

export default Ingredients;
