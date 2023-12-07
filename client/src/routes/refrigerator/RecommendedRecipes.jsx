import RecommendedRecipe from "./RecommendedRecipe";

const RecommendedRecipes = ({ recommendedRecipes }) => {
  return (
    <>
      <div className="absolute bg-white/80 top-[450px] right-[80px] min-h-[580px] -translate-y-[320px] px-12 pt-10 rounded-2xl opacity-85 shadow-[0_8px_30px_rgb(0,0,0,0.12)]">
        <header className="px-12 flex flex-row justify-between text-[18px] text-primary/80 font-bold mb-4">
          <span>Description</span>
          <span>Cuisine</span>
        </header>
        <section className="w-[400px] h-[480px] max-h-[480px] px-8 py-2 border-[#E7EEF2] border-2 rounded-md overflow-y-auto">
          {recommendedRecipes.map((recipe) => (
            <RecommendedRecipe key={recipe.recipe_id} recipe={recipe} />
          ))}
        </section>
      </div>
    </>
  );
};

export default RecommendedRecipes;
