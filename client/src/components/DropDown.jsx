import { Select, MenuItem } from "@mui/material";
import { useState } from "react";

const DropDown = ({ menuItems, setArg }) => {
  const [item, setItem] = useState(menuItems[0]);

  const handleChange = (event) => {
    setItem(event.target.value);
    setArg(event.target.value);
  };

  return (
    <>
      <Select
        value={item}
        onChange={handleChange}
        renderValue={(value) => (value ? value : "None")}
        sx={{
          marginTop: 35,
          width: 250,
          height: 50,
        }}
      >
        {menuItems.map((item, idx) => (
          <MenuItem key={idx} value={item}>
            {item}
          </MenuItem>
        ))}
      </Select>
    </>
  );
};

export default DropDown;
