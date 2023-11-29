import { useState, useEffect } from "react";
import { memo } from "react";
import axios from "axios";
import { dummyReviews } from "../../constants/Constant";

const ReviewList = ({ reviews }) => {
  return (
    <div className="h-[600px] pt-12 p-20 overflow-y-auto">
      {reviews.map((review) => {
        return (
          <div className="w-full mb-4 py-3 px-5 bg-white rounded-3xl shadow-[0px_10px_1px_rgba(221,_221,_221,_1),_0_10px_20px_rgba(204,_204,_204,_1)]">
            <div className="text-xl text-black/90">{review.content}</div>
            <div className="text-md text-black/90 text-right pr-4">
              {review.username}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default memo(ReviewList);
