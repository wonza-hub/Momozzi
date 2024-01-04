import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Description from "./Description";
import Ingredients from "./Ingredients";
import Steps from "./Steps";
import ReviewPage from "./ReviewPage";
import { FaPencilAlt } from "react-icons/fa";
import { IoCloseOutline } from "react-icons/io5";
import { MdOutlineTimer } from "react-icons/md";
import axios from "axios";

/**
 * 레시피 상세 페이지
 */
const Recipe = () => {
  const { postId } = useParams();

  const [cookTime, setCookTime] = useState("");
  const [description, setDescription] = useState("");
  const [steps, setSteps] = useState([]);
  const [ingredients, setIngredients] = useState([]);

  useEffect(() => {
    // GET: 레시피 단건 조회
    const dataUrl = `${process.env.REACT_APP_SERVER}/api/recipe/?recipe_id=${postId}`;
    axios
      ?.get(dataUrl, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        setCookTime(res.data[0].cook_time);
        setDescription(res.data[0].description);
        const processSteps = res.data[0].process.split(".");
        setSteps(processSteps);
      });
    // GET: 레시피 재료 조회
    const recipeURL = `${process.env.REACT_APP_SERVER}/api/recipe_needs_ingredient/?recipe_id=${postId}`;
    axios?.get(recipeURL)?.then((res) => {
      setIngredients(res.data);
    });
  }, [postId]);

  // 리뷰창 토글
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
              <ReviewPage></ReviewPage>
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
                className="w-full h-full contrast-120 brightness-95 object-contain"
                src={`/img/${postId}.png`}
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
