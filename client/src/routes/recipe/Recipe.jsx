import { useState, useEffect } from "react";
import { useParams, useLocation } from "react-router-dom";
import Description from "./Description";
import Ingredients from "./Ingredients";
import Steps from "./Steps";
import ReviewList from "./ReviewList";
import ReviewRegistration from "./ReviewRegistration";
import { FaPencilAlt } from "react-icons/fa";
import { IoCloseOutline } from "react-icons/io5";
import { MdOutlineTimer } from "react-icons/md";
import axios from "axios";

// dummy
import bg from "../../img/fridge_bg.png";
// import { dummyReviews } from "../../constants/Constant";

const Recipe = () => {
  const { reviewId } = useParams();
  const location = useLocation();
  const {
    cook_time: cookTime,
    description,
    process,
    thumbnailURL,
  } = location.state.recipe;
  const steps = process.split(".");

  const [ingredients, setIngredients] = useState([]);

  const [reviews, setReviews] = useState([]);

  // 레시피 단건 조회
  //   const recipeURL = `${process.env.REACT_APP_SERVER}/recipe/${reviewId}`;
  //   useEffect(() => {
  //     axios?.get(recipeURL)?.then((res) => {
  //       setIngredients(res.data.response);
  //     });
  //   }, [recipeURL]);

  // 리뷰창 토글
  const [isReviewOpen, setIsReviewOpen] = useState(false);
  const handleReviewOpen = () => {
    setIsReviewOpen(true);
  };
  const handleReviewClose = () => setIsReviewOpen(false);

  // 레시피 리뷰 목록 조회
  const reviewURL = `${process.env.REACT_APP_SERVER}/recipe/${reviewId}/review`;
  useEffect(() => {
    // // set dummy
    // setReviews(dummyReviews);

    axios?.get(reviewURL)?.then((res) => {
      setReviews(res.data);
    });
  }, []);

  return (
    <>
      <div className="flex flex-row">
        <div className="relative w-1/2 pt-[100px] h-screen bg-primary/20 flex flex-col">
          {isReviewOpen ? (
            <>
              <ReviewList reviews={reviews}></ReviewList>
              <ReviewRegistration setReviews={setReviews}></ReviewRegistration>
              <button
                className="absolute right-8 bottom-8 w-14 h-14 bg-primary/80 hover:bg-primary/90 rounded-full"
                onClick={handleReviewClose}
              >
                <IoCloseOutline className="m-auto text-3xl text-white/90" />
              </button>
            </>
          ) : (
            <>
              <img
                className="w-full h-full contrast-120 brightness-95"
                src={bg}
                alt=""
              />
              <div className="absolute right-8 bottom-24 w-14 h-14 pt-2 bg-primary/90 rounded-full text-center">
                <MdOutlineTimer className="m-auto text-2xl text-white/90" />
                <span className="text-white">{cookTime}</span>
              </div>
              <button
                className="absolute right-8 bottom-8 w-14 h-14 bg-primary/90 hover:bg-primary rounded-full"
                onClick={handleReviewOpen}
              >
                <FaPencilAlt className="m-auto text-2xl text-white/90" />
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
