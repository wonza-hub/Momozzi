import ReviewList from "./ReviewList";
import ReviewRegistration from "./ReviewRegistration";
import { useState } from "react";
import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const ReviewPage = () => {
  const { data: reviews, isLoading: isReadingReviews } = useGetReviews();

  const handleDeleteReview = (reviewId) => {
    const updatedReviews = reviews.filter(
      (review) => review.review_id !== reviewId
    );
    // setReviews(updatedReviews);
  };

  return (
    <>
      <ReviewList
        reviews={reviews}
        isReadingReviews={isReadingReviews}
      ></ReviewList>
      <ReviewRegistration />
    </>
  );
};

// REST: 리뷰 목록 조회
const useGetReviews = () => {
  const { postId } = useParams();

  return useQuery({
    queryKey: ["recipe-reviews"],
    queryFn: async () => {
      const reviewURL = `${process.env.REACT_APP_SERVER}/api/review/?recipe_id=${postId}`;
      return await axios.get(reviewURL).then((res) => res.data);
    },
  });
};

export default ReviewPage;
