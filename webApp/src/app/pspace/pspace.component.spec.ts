import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PSpaceComponent } from './pspace.component';

describe('PSpaceComponent', () => {
  let component: PSpaceComponent;
  let fixture: ComponentFixture<PSpaceComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PSpaceComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PSpaceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
