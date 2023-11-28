import { useState, useEffect } from "react";
import { useParams, useLocation } from "react-router-dom";
import Description from "./Description";
import Ingredients from "./Ingredients";
import Steps from "./Steps";
import bg from "../../img/fridge_bg.png";

import axios from "axios";

const Recipe = () => {
  const { postId } = useParams();
  const location = useLocation();
  const { cookTime, description, process, thumbnailURL } =
    location.state.recipe;
  const steps = process.split(".");

  const [ingredients, setIngredients] = useState([]);

  // 레시피 단건 조회
  //   const recipeURL = `${process.env.REACT_APP_SERVER}/recipe/${postId}`;
  //   useEffect(() => {
  //     axios?.get(recipeURL)?.then((res) => {
  //       setIngredients(res.data.response);
  //     });
  //   }, [recipeURL]);

  return (
    <>
      <div className="flex flex-row">
        <div className="w-1/2 pt-[100px] h-screen bg-backgroundGray/20">
          <img className="w-full h-full" src={bg} alt="" />
        </div>
        <div className="w-1/2 pt-[100px] h-screen bg-backgroundGray/20 overflow-y-scroll">
          <div className="pt-[32px] px-[40px]">
            <Description description={description}></Description>
            <Ingredients ingredients={ingredients}></Ingredients>
            <Steps steps={steps}></Steps>
          </div>
        </div>
      </div>
    </>
  );
};

export default Recipe;
