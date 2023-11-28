import { useState, useEffect } from "react";
import { useParams, useLocation } from "react-router-dom";
import Description from "./Description";
import Ingredients from "./Ingredients";
import Steps from "./Steps";
import ReviewList from "./ReviewList";
import { FaPencilAlt } from "react-icons/fa";
import { IoCloseOutline } from "react-icons/io5";
import axios from "axios";
import bg from "../../img/fridge_bg.png";

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

  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const handleReviewOpen = () => {
    setIsReviewOpen(true);
  };
  const handleReviewClose = () => setIsReviewOpen(false);

  return (
    <>
      <div className="flex flex-row">
        <div className="relative w-1/2 pt-[100px] h-screen bg-primary/20 flex flex-col">
          {isReviewOpen ? (
            <>
              <ReviewList postId={postId}></ReviewList>
              <form action="submit"></form>
              <button
                className="absolute right-8 bottom-8 w-14 h-14 bg-primary/80 hover:bg-primary/90 rounded-full"
                onClick={handleReviewClose}
              >
                <IoCloseOutline className="m-auto text-3xl text-white/90" />
              </button>
            </>
          ) : (
            <>
              <img className="w-full h-full" src={bg} alt="" />
              <button
                className="absolute right-8 bottom-8 w-14 h-14 bg-primary/80 hover:bg-primary/90 rounded-full"
                onClick={handleReviewOpen}
              >
                <FaPencilAlt className="m-auto text-3xl text-white/90" />
              </button>
            </>
          )}
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
