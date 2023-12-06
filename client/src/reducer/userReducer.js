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
      state.first_name = action.payload[0].first_name;
      state.last_name = action.payload[0].last_name;
      state.id = action.payload[0].user_id;
      state.name = state.first_name + state.last_name;
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
