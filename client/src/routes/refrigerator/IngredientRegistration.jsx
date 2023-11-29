import { useState, useRef } from "react";
import { redirect } from "react-router-dom";
import axios from "axios";

const IngredientRegistration = () => {
  const [newIngredient, setNewIngredient] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const ingredientInputRef = useRef(null);

  const handleIngredientInputChange = () => {
    setNewIngredient(ingredientInputRef.current.value);
  };

  const addIngredient = (event) => {
    event.preventDefault();

    if (!newIngredient) {
      return;
    }
    const ingredientPostURL = `${process.env.REACT_APP_SERVER}/`;
    axios
      ?.post(ingredientPostURL, newIngredient)
      ?.then((res) => {
        if (res.status === 200) {
          return redirect("/refrigerator");
        }
      })
      ?.catch(() => console.log("post fail"));
  };

  return (
    <>
      <form
        className="flex flex-row justify-end mt-8 mb-12"
        onSubmit={addIngredient}
      >
        {isLoading ? (
          <div class="w-full h-full pt-2 pb-1 flex justify-center">
            {/* <LoadingSpinner></LoadingSpinner> */}
          </div>
        ) : (
          <input
            onChange={handleIngredientInputChange}
            value={newIngredient}
            className="w-44 h-12 mr-6 px-4 py-2 bg-[#efefef] border-none rounded-xl outline-2 outline-primary text-xl text-black/90 hover:bg-[#efefef]/70"
            type="text"
            placeholder="재료 추가"
            ref={ingredientInputRef}
          />
        )}
        <button
          className="w-32 h-12 px-4 my-auto bg-primary/90 text-xl text-white rounded-xl hover:bg-primary"
          type="submit"
        >
          Add
        </button>
      </form>
    </>
  );
};

export default IngredientRegistration;
