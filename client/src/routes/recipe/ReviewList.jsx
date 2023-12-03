import { memo } from "react";
import Review from "./Review";

const ReviewList = ({ reviews }) => {
  return (
    <div className="h-[600px] pt-12 p-20 overflow-y-auto">
      {reviews.map((review) => (
        <Review review={review}></Review>
      ))}
    </div>
  );
};

export default memo(ReviewList);
