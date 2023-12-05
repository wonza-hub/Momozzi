import StoredIngredient from "./StoredIngredient";

/**
 * 냉장고 내 재료 목록 컴포넌트
 * @param {storedIngredients}
 * @returns
 */
const Inventory = ({ storedIngredients }) => {
  return (
    <>
      <header className="px-32 flex flex-row justify-between text-[18px] text-primary/80 font-bold mb-4">
        <span>Type</span>
        <span>Name</span>
        <span>Calories</span>
      </header>
      <section className="w-[720px] h-[320px] max-h-[320px] px-32 py-2 border-[#E7EEF2] border-2 rounded-md overflow-y-auto">
        {storedIngredients.map((storedIngredient) => (
          <StoredIngredient ingredient={storedIngredient} />
        ))}
      </section>
    </>
  );
};

export default Inventory;
