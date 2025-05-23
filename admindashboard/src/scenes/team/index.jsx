import {Box, Typography, useTheme} from "@mui/material";
import {DataGrid} from "@mui/x-data-grid";
import { tokens } from "../../theme";
import {mockDataTeam} from "../../data/mockData";
import AdminPanelSettingsOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import LockOpenOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import SecurtiyOutlinedIcon from "@mui/icons-material/AdminPanelSettingsOutlined";
import Header from "../../components/Header";

const Team = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const columns = [
        {
            field: "id", 
            headerName : "ID"
        },
        {
            field: "name", 
            headerName : "Name", 
            flex : 1, 
            cellClassName: "name-column--cell",
        }, 
        {
            field: "age", 
            headerName : "Age", 
            type : "number", 
            headerAlign : "left", 
            align : "left",
        }, 
        {
            field: "phone", 
            headerName : "Phone Number", 
            flex : 1,
        },
        {
            field: "email", 
            headerName : "Email", 
            flex : 1,
        },
        {
            field: "accessLevel", 
            headerName : "Access Level", 
            flex : 1, 
            renderCell : ({row : {access}}) => {
                return (
                    <Box
                        width="60%"
                        m = "10px auto"
                        p = "5px"
                        display = "flex"
                        justifyContent= "center"
                        backgroundColor = {
                            access === "admin"
                              ? '#de796e'
                              : '#44b29a'
                        }
                        borderRadius= "4px"
                    >
                        {access === "admin" && <AdminPanelSettingsOutlinedIcon />}
                        {access === "manager" && <SecurtiyOutlinedIcon />}
                        {access === "agent" && <LockOpenOutlinedIcon />}
                        <Typography color = {colors.gray[100]} sx={{ml : "5px"}}>
                            {access}
                        </Typography>


                    </Box>
                );
            },
        },
    ];

    return (
        <Box m = "20px">
            <Header title = "TEAM" subtitle= {<span style={{ color: colors.blueAccent[300] }}>Managing the Team Members</span>} />
            <Box m = "40px 0 0 0" height = "75vh" sx = {{
                "& .MuiDataGrid-root": {
                    border : "none"
                },
                "& .MuiDataGrid-cell" : {
                    borderBottom : "none"
                },
                "& .name-column--cell": {
                    color : colors.blueAccent[100]
                },
                "& .MuiDataGrid-columnHeader":{
                    backgroundColor : colors.blueAccent[500],
                    borderBottom : "none"
                },
                "& .MuiDataGrid-virtualScroller": {
                    backgroundColor : colors.primary[400]
                },
                "& .MuiDataGrid-footerContainer": {
                    borderTop : "none",
                    backgroundColor : colors.blueAccent[500]
                },
            }}>
               <DataGrid
               rows = {mockDataTeam}
               columns={columns}
               /> 
            </Box>
        </Box>
    )

}


export default Team;