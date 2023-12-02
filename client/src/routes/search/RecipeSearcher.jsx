import SearchBar from "./SearchBar";
import RecipeList from "./RecipeList";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import axios from "axios";
// dummy
import { dummyRecipe } from "../../constants/Constant";

const RecipeSearcher = () => {
  const location = useLocation();
  const foodFilter = location.state && location.state.foodFilter;
  const { method, category } = foodFilter || {};

  const [recipes, setRecipes] = useState([]);

  // // set dummy recipe
  // useEffect(() => {
  //   setRecipes(dummyRecipe);
  // }, []);

  useEffect(() => {
    if (method || category) {
      const recommendUrl = `${process.env.REACT_APP_SERVER}/`;
      axios?.get(recommendUrl)?.then((res) => {
        setRecipes(res.data);
      });
    } else {
      const dataUrl = `${process.env.REACT_APP_SERVER}/api/recipe/`;
      axios
        ?.get(dataUrl, {
          headers: {
            "Content-Type": "application/json",
          },
        })
        ?.then((res) => {
          console.log(res.data);
          setRecipes(res.data);
        });
    }
  }, [method, category]);

  return (
    <>
      <div className="flex flex-row">
        <SearchBar setRecipes={setRecipes}></SearchBar>
        <RecipeList recipes={recipes}></RecipeList>
      </div>
    </>
  );
};

export default RecipeSearcher;
