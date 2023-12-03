const Ingredients = ({ ingredients }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-sm">
        Ingredients
      </header>
      <div className="ingredients mb-8 font-semibold text-xl text-white flex flex-row overflow-x-scroll">
        {ingredients.map((ingredient) => (
          <div
            className="w-fit h-11 mr-6 px-2 bg-secondary text-center leading-10 rounded-2xl"
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
