import { useState, useEffect } from "react";
import { memo } from "react";
import axios from "axios";
import Review from "./Review";

import { dummyReviews } from "../../constants/Constant";

const ReviewList = ({ reviews }) => {
  return (
    <div className="h-[600px] pt-12 p-20 overflow-y-auto">
      {dummyReviews.map((review) => (
        <Review review={review}></Review>
      ))}
    </div>
  );
};

export default memo(ReviewList);
