import React from 'react'
import LandingPage from './LandingPage'
import AnalysisResults from "./AnalysisResults";
import {withRouter, Route, Switch} from 'react-router-dom'
import { Container, Segment } from 'semantic-ui-react';

const App = () => {
  return (
    <Container fluid>
      <br />
      <Switch>
        <Route exact path='/' component={LandingPage}/>
        <Route path='/analysis' component={AnalysisResults} />
      </Switch>
    </Container>
  )
}

export default withRouter(App)
