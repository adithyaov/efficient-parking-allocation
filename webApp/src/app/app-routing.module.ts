import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GetLotsComponent } from './get-lots/get-lots.component';
import { DefineLotsComponent } from './define-lots/define-lots.component';
import { BuildingsComponent } from './buildings/buildings.component';

const routes: Routes = [
    { path: 'get-lots', component: GetLotsComponent },
    { path: 'define-lots', component: DefineLotsComponent },
    { path: 'buildings', component: BuildingsComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
