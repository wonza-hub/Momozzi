const Ingredients = ({ ingredients }) => {
  return (
    <>
      <header className="mb-5 text-3xl font-bold text-primary drop-shadow-sm">
        Ingredients
      </header>
      <div className="ingredients pb-2 mb-8 font-semibold text-xl text-white flex flex-row overflow-x-auto">
        {ingredients.map((ingredient) => (
          <div className="w-28 h-10 mr-6 bg-secondary text-center leading-10 rounded-2xl">
            {ingredient}
          </div>
        ))}
      </div>
    </>
  );
};

export default Ingredients;
