import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DefineLotsComponent } from './define-lots.component';

describe('DefineLotsComponent', () => {
  let component: DefineLotsComponent;
  let fixture: ComponentFixture<DefineLotsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DefineLotsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DefineLotsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
