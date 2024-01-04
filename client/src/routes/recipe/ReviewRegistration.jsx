import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import CircularProgress from "@mui/material/CircularProgress";
import { useSelector } from "react-redux";
import { useQueryClient, useMutation } from "@tanstack/react-query";

/**
 * 리뷰 작성
 * @param {*} param0
 * @returns
 */
const ReviewRegistration = () => {
  const { postId } = useParams();

  const user = useSelector((state) => state.user);

  const [newReview, setNewReview] = useState("");
  const [newReviewData, setNewReviewData] = useState({
    content: newReview,
    user_id: user.id,
    recipe_id: postId,
    last_name: user.last_name,
  });

  const reviewInputRef = useRef(null);
  const handleReviewInputChange = () => {
    setNewReview(reviewInputRef.current.value);
    setNewReviewData({
      content: reviewInputRef.current.value,
      user_id: user.id,
      recipe_id: postId,
      last_name: user.last_name,
    });
  };

  const { mutate: createReview, isPending } = usePostReview();

  const handleReviewSubmit = (event) => {
    event.preventDefault();
    if (!user.id) {
      alert("로그인 후 리뷰를 작성해주세요.");

      return;
    }
    createReview(newReviewData);
    setNewReview("");
  };

  return (
    <>
      <form className="flex-auto mr-2" onSubmit={handleReviewSubmit}>
        {isPending ? (
          <div className="w-full h-full flex justify-center items-center">
            <CircularProgress color="success" />
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

// REST: 리뷰 등록
const usePostReview = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (newReviewData) => {
      const reviewPostURL = `${process.env.REACT_APP_SERVER}/api/review/`;
      return await axios.post(reviewPostURL, newReviewData);
    },
    onSuccess: () => {
      queryClient.invalidateQueries(["recipe-reviews"]);
    },
  });
};

export default ReviewRegistration;
