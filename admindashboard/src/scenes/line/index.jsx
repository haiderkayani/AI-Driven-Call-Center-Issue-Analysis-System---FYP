import { Box } from "@mui/material";
import Header from "../../components/Header";
import LineChart from "../../components/LineChart";

const Line = () => {
  return (
    <Box m="20px">
      <Header title="Overall Call Volume" />
      <Box height="70vh">
        <LineChart />
      </Box>
    </Box>
  );
};

export default Line;