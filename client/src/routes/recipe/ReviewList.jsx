import { memo } from "react";
import ReviewListItem from "./ReviewListItem";

const ReviewList = ({ reviews, isReadingReviews }) => {
  return (
    <>
      {isReadingReviews ? null : (
        <div className="h-[600px] pt-12 p-20 overflow-y-auto">
          {reviews.map((review) => (
            <ReviewListItem
              review={review}
              isReadingReviews={isReadingReviews}
            ></ReviewListItem>
          ))}
        </div>
      )}
    </>
  );
};

export default memo(ReviewList);
