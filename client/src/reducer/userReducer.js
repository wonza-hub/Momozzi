import { createSlice } from "@reduxjs/toolkit";

export const userReducer = createSlice({
  name: "user",
  initialState: {
    name: "",
    id: "",
    isLoading: false,
    isLogin: null,
  },
  reducers: {
    loginUser: (state, action) => {
      state.id = action.payload[0][0];
      state.name = action.payload[0][1];
      state.isLogin = true;
    },

    clearUser: (state) => {
      state.name = "";
      state.id = "";
      state.isLogin = false;
    },
  },
});

export const { loginUser, clearUser } = userReducer.actions;
export default userReducer;
