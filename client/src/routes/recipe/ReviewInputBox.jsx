import { useState, useRef } from "react";
import { redirect, useParams } from "react-router-dom";
import axios from "axios";

const ReviewInputBox = ({ setReviews }) => {
  const { reviewPostId } = useParams();

  const [isLoading, setIsLoading] = useState(false);
  const [newReview, setNewReview] = useState("");

  const reviewInputRef = useRef(null);

  const handleReviewInputChange = () => {
    setNewReview(reviewInputRef.current.value);
  };

  const handleReviewSubmit = (event) => {
    event.preventDefault();

    const reviewPostURL = `${process.env.REACT_APP_SERVER}/review/${reviewPostId}`;
    axios
      ?.post(reviewPostURL, newReview)
      ?.then((res) => {
        if (res.status === 200) {
          return redirect(`/recipe/${reviewPostId}`);
        }
      })
      ?.catch(() => console.log("post fail"));
  };

  return (
    <>
      <form className="flex-auto mr-2" onSubmit={handleReviewSubmit}>
        {isLoading ? (
          <div class="w-full h-full pt-2 pb-1 flex justify-center">
            {/* <LoadingSpinner></LoadingSpinner> */}
          </div>
        ) : (
          <input
            onChange={handleReviewInputChange}
            value={newReview}
            className="w-full h-full py-0 pl-10 pr-24 bg-[#efefef] border-none rounded-3xl outline-2 outline-primary text-xl text-black/90"
            type="text"
            placeholder="리뷰 추가"
            ref={reviewInputRef}
          />
        )}
      </form>
    </>
  );
};

export default ReviewInputBox;
