import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GetLotsComponent } from './get-lots/get-lots.component';

const routes: Routes = [
    { path: 'get-lots', component: GetLotsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
