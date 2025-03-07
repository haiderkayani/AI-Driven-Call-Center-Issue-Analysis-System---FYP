import { CssBaseline, ThemeProvider} from "@mui/material";
import { ColorModeContext, useMode } from "./theme";
import {Routes, Route} from "react-router-dom";
import Topbar from "./scenes/global/Topbar";
import Navbar from "./scenes/global/Navbar";
import Dashboard from "./scenes/dashboard"
import IssueStatus from "./scenes/issuestatus"
import Team from "./scenes/team"
import Contacts from "./scenes/contacts"
import Form from "./scenes/form"
// import Line from "./scenes/line"
// import FAQ from "./scenes/faq"
import Bar from "./scenes/bar"
import Pie from "./scenes/pie"
// import Geography from "./scenes/geography"
// import Calendar from "./scenes/calendar"

function App() {
  const [theme, colorMode] = useMode();

  return (
    <ColorModeContext.Provider value ={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <div className="app">
          <Navbar />
          <main className="content">
            <Topbar />
            <Routes>
              <Route path='/' element={<Dashboard />} />
              <Route path='/team' element={<Team />} /> 
              <Route path='/issuestatus' element={<IssueStatus />} />
              <Route path='/contacts' element={<Contacts />} />
              <Route path='/form' element={<Form />} />
              {/* <Route path='/line' element={<Line />} /> */}
              {/* <Route path='/faq' element={<FAQ />} /> */}
              <Route path='/bar' element={<Bar />} />
              <Route path='/pie' element={<Pie />} />
              {/* <Route path='/geography' element={<Geography />} /> */}
              {/* <Route path='/calendar' element={<Calendar />} /> */}
            </Routes>
          </main>
        </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
  );
}

export default App;
