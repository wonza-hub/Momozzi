import { configureStore } from "@reduxjs/toolkit";
import { userReducer } from "./reducer/userReducer";

const store = configureStore({
  reducer: {
    user: userReducer.reducer,
  },
});

export default store;
