const StoredIngredient = ({ ingredient }) => {
  return (
    <div className="text-lg my-2 flex flex-row justify-between text-[#111111]">
      <span className="ingredientType">{ingredient.type}</span>
      <span className="ingredientName text-left">{ingredient.name}</span>
      <span className="ingredientName">{ingredient.calories}</span>
    </div>
  );
};

export default StoredIngredient;
