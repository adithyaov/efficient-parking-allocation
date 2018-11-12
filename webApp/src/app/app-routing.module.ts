import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GetLotsComponent } from './get-lots/get-lots.component';
import { DefineLotsComponent } from './define-lots/define-lots.component';
import { BuildingsComponent } from './buildings/buildings.component';
import { InterconnectsComponent } from './interconnects/interconnects.component';
import { CameraGuideComponent } from './camera-guide/camera-guide.component';
import { AdminComponent } from './admin/admin.component';
import { PSpaceComponent } from './pspace/pspace.component';
import { HomeComponent } from './home/home.component';

const routes: Routes = [
    { path: '', component: HomeComponent},
    { path: 'get-lots', component: GetLotsComponent },
    { path: 'define-lots', component: DefineLotsComponent },
    { path: 'buildings', component: BuildingsComponent },
    { path: 'interconnects', component: InterconnectsComponent },
    { path: 'camera-guide', component: CameraGuideComponent },
    { path: 'admin', component: AdminComponent },
    { path: 'define-pspace', component: PSpaceComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
