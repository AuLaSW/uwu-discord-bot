use pyo3::prelude::*;
use uwuifier::uwuify_str_sse;

// passes a string to uwuify and returns the value
#[pyfunction]
fn uwuify(a: &str) -> PyResult<String> {
    Ok(uwuify_str_sse(a))
}

/// A Python module implemented in Rust.
#[pymodule]
fn uwu(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(uwuify, m)?)?;
    Ok(())
}
