import { TestBed } from '@angular/core/testing';
<<<<<<< HEAD
=======
import { provideHttpClient } from '@angular/common/http';
import { provideRouter } from '@angular/router';

>>>>>>> ticket-project-update
import { App } from './app';

describe('App', () => {
  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [App],
<<<<<<< HEAD
=======
      providers: [provideHttpClient(), provideRouter([])],
>>>>>>> ticket-project-update
    }).compileComponents();
  });

  it('should create the app', () => {
    const fixture = TestBed.createComponent(App);
    const app = fixture.componentInstance;
    expect(app).toBeTruthy();
  });

  it('should render title', async () => {
    const fixture = TestBed.createComponent(App);
    await fixture.whenStable();
    const compiled = fixture.nativeElement as HTMLElement;
<<<<<<< HEAD
    expect(compiled.querySelector('h1')?.textContent).toContain('Hello, project_web');
=======
    expect(compiled.querySelector('h1')?.textContent).toContain('Formula 1 tickets');
>>>>>>> ticket-project-update
  });
});
