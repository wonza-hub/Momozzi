import { useEffect, memo } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";
import Review from "./Review";

const ReviewList = ({ reviews, setReviews }) => {
  const { postId } = useParams();

  const handleDeleteReview = (reviewId) => {
    const updatedReviews = reviews.filter(
      (review) => review.review_id !== reviewId
    );
    setReviews(updatedReviews);
  };

  // GET: 레시피 리뷰
  useEffect(() => {
    const reviewURL = `${process.env.REACT_APP_SERVER}/api/review/?recipe_id=${postId}`;
    axios?.get(reviewURL)?.then((res) => {
      setReviews(res.data);
    });
  }, [postId, setReviews]);

  return (
    <div className="h-[600px] pt-12 p-20 overflow-y-auto">
      {reviews.map((review) => (
        <Review review={review} onDeleteReview={handleDeleteReview}></Review>
      ))}
    </div>
  );
};

export default memo(ReviewList);
