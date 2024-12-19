import {Box , Typography, useTheme} from "@mui/material";
import {DataGrid} from "@mui/x-data-grid";
import { tokens } from "../../theme";
import {mockDataInvoices} from "../../data/mockData";
import Header from "../../components/Header";

const IssueStatus = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const columns = [
        {
            field: "id", 
            headerName : "ID",
        },
        {
            field: "agentName", 
            headerName : "Agent Name", 
            flex : 1, 
            cellClassName: "name-column--cell",
        }, 
       
        {
            field: "category", 
            headerName : "Category", 
            flex : 1,
        },
        {
            field: "area", 
            headerName : "Area", 
            flex : 1,
        },
        {
            field : "status",
            headerName : "Status",
            flex : 1,

            renderCell : ({row : {status}}) => {
                return (
                    <Box
                        width="60%"
                        m = "10px auto"
                        p = "5px"
                        display = "flex"
                        justifyContent= "center"
                        backgroundColor = {
                            status === "Unresolved"
                              ? '#de796e'
                              : '#e09991'
                        }
                        borderRadius= "4px"
                    >
                        {status === "Resolved"}
                        {status === "In-Progress"}
                        {status === "Unresolved"}
                        <Typography color = {colors.gray[100]} sx={{ml : "5px"}}>
                            {status}
                        </Typography>


                    </Box>
                );
            },
        },
        {
            field : "date",
            headerName : "Date",
            flex : 1,
        },
    ];

    return (
        <Box m = "20px">
            <Header title = "Issue Status" subtitle= {<span style={{ color: colors.blueAccent[300] }}>Status of the Issues being Reported</span>} />
            <Box m = "40px 0 0 0" height = "75vh" sx = {{
                    "& .MuiDataGrid-root": {
                        border : "none"
                    },
                    "& .MuiDataGrid-cell" : {
                        borderBottom : "none"
                    },
                    "& .name-column--cell": {
                        color : colors.blueAccent[200]
                    },
                    "& .MuiDataGrid-columnHeader":{
                        backgroundColor : colors.blueAccent[400],
                        borderBottom : "none"
                    },
                    "& .MuiDataGrid-virtualScroller": {
                        backgroundColor : colors.primary[400]
                    },
                    "& .MuiDataGrid-footerContainer": {
                        borderTop : "none",
                        backgroundColor : colors.blueAccent[400]
                    },
                    "&MultiCheckbox-root" : {
                        color : `${colors.greenAccent[200]} !important`,
                    },
                    "& .MuiDataGridCheckbox-root":{
                        color: `${colors.greenAccent[200]} !important`,
                    },
                }}
            >
               <DataGrid
               checkboxSelection
               rows = {mockDataInvoices}
               columns={columns}
               /> 
            </Box>
        </Box>
    )

}


export default IssueStatus;