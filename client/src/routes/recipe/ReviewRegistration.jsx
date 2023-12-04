import { useState, useRef } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import CircularProgress from "@mui/material/CircularProgress";
import { useSelector } from "react-redux";

const ReviewRegistration = ({ setReviews }) => {
  const { postId } = useParams();

  const user = useSelector((state) => state.user);

  const [isLoading, setIsLoading] = useState(false);
  const [newReview, setNewReview] = useState("");

  const reviewInputRef = useRef(null);

  const handleReviewInputChange = () => {
    setNewReview(reviewInputRef.current.value);
  };

  const handleReviewSubmit = (event) => {
    if (!user.id) {
      alert("로그인 후 리뷰를 작성해주세요.");
      event.preventDefault();
      return;
    }
    event.preventDefault();
    setIsLoading(true);

    let reviewBody = {
      content: newReview,
      user_id: user.id,
      recipe_id: postId,
    };

    const reviewPostURL = `${process.env.REACT_APP_SERVER}/api/review/`;
    axios
      ?.post(reviewPostURL, reviewBody, {
        headers: {
          "Content-Type": "application/json",
        },
      })
      ?.then((res) => {
        // 댓글 등록 성공시 리로딩
        if (res.status === 200) {
          setIsLoading(false);
          setNewReview("");
          const reviewURL = `${process.env.REACT_APP_SERVER}/api/review/?recipe_id=${postId}`;
          axios?.get(reviewURL)?.then((res) => {
            setReviews(res.data);
          });
        }
      })
      ?.catch(() => console.log("post fail"));
  };

  return (
    <>
      <form className="flex-auto mr-2" onSubmit={handleReviewSubmit}>
        {isLoading ? (
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

export default ReviewRegistration;
