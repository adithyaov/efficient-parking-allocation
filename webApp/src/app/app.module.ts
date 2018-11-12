import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FileSelectDirective } from 'ng2-file-upload';
import { FormsModule } from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './nav/nav.component';
import { GetLotsComponent } from './get-lots/get-lots.component';
import { DefineLotsComponent } from './define-lots/define-lots.component';
import { BuildingsComponent } from './buildings/buildings.component';
import { InterconnectsComponent } from './interconnects/interconnects.component';
import { CameraGuideComponent } from './camera-guide/camera-guide.component';
import { AdminComponent } from './admin/admin.component';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    GetLotsComponent,
    FileSelectDirective,
    DefineLotsComponent,
    BuildingsComponent,
    InterconnectsComponent,
    CameraGuideComponent,
    AdminComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
